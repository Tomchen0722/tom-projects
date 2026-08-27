document.addEventListener('DOMContentLoaded', () => {
  // Create the floating TTS button
  const ttsBtn = document.createElement('div');
  ttsBtn.innerHTML = '🔊 發音';
  ttsBtn.style.position = 'absolute';
  ttsBtn.style.display = 'none';
  ttsBtn.style.backgroundColor = '#0284c7';
  ttsBtn.style.color = '#fff';
  ttsBtn.style.padding = '4px 8px';
  ttsBtn.style.borderRadius = '4px';
  ttsBtn.style.fontSize = '14px';
  ttsBtn.style.cursor = 'pointer';
  ttsBtn.style.boxShadow = '0 2px 4px rgba(0,0,0,0.2)';
  ttsBtn.style.zIndex = '9999';
  document.body.appendChild(ttsBtn);

  let currentText = '';

  // Function to show button near selection
  const handleSelection = (e) => {
    setTimeout(() => {
      const selection = window.getSelection();
      const text = selection.toString().trim();
      
      // If there's text and it contains English characters
      if (text && /[a-zA-Z]/.test(text)) {
        currentText = text;
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        
        // Calculate position (above the selection)
        const top = rect.top + window.scrollY - 30;
        const left = rect.left + window.scrollX + (rect.width / 2) - 30;
        
        ttsBtn.style.top = `${top > 0 ? top : 0}px`;
        ttsBtn.style.left = `${left > 0 ? left : 0}px`;
        ttsBtn.style.display = 'block';
      } else {
        ttsBtn.style.display = 'none';
      }
    }, 10);
  };

  // Hide button when clicking outside
  document.addEventListener('mousedown', (e) => {
    if (e.target !== ttsBtn) {
      ttsBtn.style.display = 'none';
    }
  });

  // Re-check selection on mouseup
  document.addEventListener('mouseup', handleSelection);
  // Also check on keyboard selection (Shift + arrows)
  document.addEventListener('keyup', (e) => {
    if (e.key === 'Shift' || e.key.startsWith('Arrow')) {
      handleSelection();
    }
  });

  // Prevent the click from clearing the selection
  ttsBtn.addEventListener('mousedown', (e) => {
    e.preventDefault();
  });

  ttsBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    window.speakEn(currentText);
  });

  // Global speak function for backward compatibility with existing inline buttons
  window.speakEn = (text) => {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.7; // Slower speed
    window.speechSynthesis.speak(utterance);
  };
});
