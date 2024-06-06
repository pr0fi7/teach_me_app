# cards/views.py
from .models import Card
from .forms import DocumentUploadForm, CardCreateForm
from django.shortcuts import get_object_or_404, redirect, render
from io import BytesIO
from openai import OpenAI
from .utils import chunk_document, generate_flashcard_text
import pdfplumber
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openaiapi = openai.api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openaiapi)

def CardListView(request):
    cards = Card.objects.all().order_by('box')
    boxes = {}
    for card in cards:
        if card.box not in boxes:
            boxes[card.box] = []
        boxes[card.box].append(card)

    context = {"boxes": boxes, 'cards': cards}
    return render(request, "cards/card_list.html", context)

def CardCreateView(request):
    if request.method == "POST":
        form = CardCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('card-list')
    else:
        form = CardCreateForm()
    
    context = {"form": form}
    return render(request, "cards/card_form.html", context)

def SelectBoxView(request):
    boxes = Card.objects.values_list('box', flat=True).distinct()
    return render(request, 'cards/select_box.html', {'boxes': boxes})

def TrainView(request, box_num):
    cards = Card.objects.filter(box=box_num, solved=False)  # Get only unsolved cards in the selected box
    if not cards.exists():
        return render(request, 'cards/train_complete.html')  # Show a completion message if all cards are solved

    card = cards.order_by('?').first()  # Get a random unsolved card

    if request.method == "POST":
        card_id = request.POST.get('card_id')
        solved = request.POST.get('solved') == 'true'

        card = get_object_or_404(Card, id=card_id)
        card.solved = solved
        card.save()
        return render(request, 'cards/train_cards.html', {'card': card, 'show_answer': True, 'solved': solved})

    return render(request, 'cards/train_cards.html', {'card': card, 'show_answer': False})

def delete_box(request, box_num):
    if request.method == "POST":
        Card.objects.filter(box=box_num).delete()
        return redirect('card-list')
    return render(request, 'cards/confirm_delete_box.html', {'box_num': box_num})

class CardUpdateView(UpdateView):
    model = Card
    form_class = CardCreateForm
    template_name = 'cards/card_form.html'
    success_url = reverse_lazy('card-list')

def BoxView(request, box_num):
    all_boxes = Card.objects.values_list('box', flat=True).distinct()
    cards = Card.objects.filter(box=box_num)
    boxes = {}
    for card in cards:
        if card.box not in boxes:
            boxes[card.box] = []
        boxes[card.box].append(card)
    
    context = {
        "boxes": {box: [] for box in all_boxes},
        "current_box": box_num,
        "cards": cards
    }
    return render(request, "cards/box.html", context)

def upload_document(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = request.FILES['document']
            raw_data = document.read()
            slider_value = request.POST.get('slider')
            box = request.POST.get('box')  # Get the box number from the form

            # Use a BytesIO stream to read the PDF content
            pdf_stream = BytesIO(raw_data)
            
            try:
                all_text = ""
                with pdfplumber.open(pdf_stream) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        all_text += text if text else ""
                
                if not all_text.strip():
                    return render(request, 'cards/upload_document.html', {'form': form, 'error': 'Could not extract text from the uploaded PDF.'})

                # Split the text into chunks and generate flashcards
                chunks = chunk_document(all_text)
             
                for chunk in chunks:
                    flashcard_text = generate_flashcard_text(client, chunk, slider_value)
                    for question, answer in flashcard_text.items():
                        Card.objects.create(question=question, answer=answer, box=box)  # Save the card with the box number
                
                return redirect('card-list')
            except Exception as e:
                return render(request, 'cards/upload_document.html', {'form': form, 'error': f'Error processing PDF file: {str(e)}'})
    else:
        form = DocumentUploadForm()
    return render(request, 'cards/upload_document.html', {'form': form})
