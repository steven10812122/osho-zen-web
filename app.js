const IMG_PATH = 'assets/cards/';

const state = {
  currentDeckKey: 'main',
};

const deckByKey = Object.fromEntries(DECKS.map(d => [d.key, d]));
const totalCards = DECKS.reduce((sum, d) => sum + d.cards.length, 0);

const els = {
  tabs: document.querySelectorAll('.tab-btn'),
  gridView: document.getElementById('grid-view'),
  grid: document.getElementById('grid'),
  drawView: document.getElementById('draw-view'),
  drawBack: document.getElementById('draw-back'),
  drawResult: document.getElementById('draw-result'),
  drawResultImg: document.getElementById('draw-result-img'),
  drawResultText: document.getElementById('draw-result-text'),
  detailView: document.getElementById('detail-view'),
  detailImg: document.getElementById('detail-img'),
  detailText: document.getElementById('detail-text'),
  detailBack: document.getElementById('detail-back'),
};

function showView(name) {
  els.gridView.hidden = name !== 'grid';
  els.drawView.hidden = name !== 'draw';
  els.detailView.hidden = name !== 'detail';
}

function setActiveTab(deckKey) {
  els.tabs.forEach(btn => {
    btn.classList.toggle('active', btn.dataset.deck === deckKey);
  });
}

function renderGrid(deckKey) {
  const deck = deckByKey[deckKey];
  els.grid.innerHTML = '';
  deck.cards.forEach(card => {
    const img = document.createElement('img');
    img.src = IMG_PATH + card.image;
    img.alt = `${deck.label} ${card.num}`;
    img.addEventListener('click', () => openDetail(card));
    els.grid.appendChild(img);
  });
}

function openDeck(deckKey) {
  state.currentDeckKey = deckKey;
  setActiveTab(deckKey);
  renderGrid(deckKey);
  showView('grid');
}

function openDetail(card) {
  els.detailImg.src = IMG_PATH + card.image;
  els.detailText.textContent = card.text;
  showView('detail');
}

function resetDraw() {
  els.drawBack.src = IMG_PATH + CARD_BACK_IMAGE;
  els.drawResult.hidden = true;
  showView('draw');
  setActiveTab(null);
}

function drawRandomCard() {
  let index = Math.floor(Math.random() * totalCards);
  for (const deck of DECKS) {
    if (index < deck.cards.length) {
      return deck.cards[index];
    }
    index -= deck.cards.length;
  }
}

els.drawBack.addEventListener('click', () => {
  const card = drawRandomCard();
  els.drawResultImg.src = IMG_PATH + card.image;
  els.drawResultText.textContent = card.text;
  els.drawResult.hidden = false;
});

els.detailBack.addEventListener('click', () => {
  setActiveTab(state.currentDeckKey);
  showView('grid');
});

els.tabs.forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.dataset.view === 'draw') {
      resetDraw();
    } else {
      openDeck(btn.dataset.deck);
    }
  });
});

openDeck('main');
