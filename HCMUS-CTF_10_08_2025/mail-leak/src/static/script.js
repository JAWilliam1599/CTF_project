const html = document.documentElement;
html.setAttribute('data-bs-theme', 'light');

const infoButton = document.getElementById('info-button');
const infoModal = new bootstrap.Modal(document.getElementById('infoModal'));

infoButton.addEventListener('click', () => {
    infoModal.show();
});

const bodyInput = document.getElementById('prompt-input');
const sendButton = document.getElementById('send-prompt');
const charCount = document.getElementById('char-count');
const subjectInput = document.querySelector('input[placeholder="Enter email subject"]');

sendButton.addEventListener('click', sendEmail);

bodyInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendEmail();
    }
});

bodyInput.addEventListener('input', () => {
    const count = bodyInput.value.length;
    charCount.textContent = count;
    
    if (count > 900) {
        charCount.style.color = '#d13438';
    } else if (count > 800) {
        charCount.style.color = '#ff8c00';
    } else {
        charCount.style.color = '#6c757d';
    }
});

async function sendEmail() {
    const body = bodyInput.value.trim();
    if (!body) return;
    
    if (body.length > 1000) {
        alert('Message too long! Please keep it under 1000 characters.');
        return;
    }

    bodyInput.value = '';
    charCount.textContent = '0';
    charCount.style.color = '#6c757d';
    sendButton.disabled = true;
    sendButton.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Processing...';

    try {
        const subject = subjectInput.value.trim();
        const response = await fetch('/send_mail', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ body, subject })
        });
        const result = await response.json();
        if (response.ok) {
            if (result.error) {
                const botResponseContent = document.getElementById('bot-response-content');
                botResponseContent.innerHTML = `<i class="fas fa-exclamation-triangle me-2"></i>Error: ${result.error}`;
                const botReplyModal = new bootstrap.Modal(document.getElementById('botReplyModal'));
                botReplyModal.show();
            } else {
                const botResponseContent = document.getElementById('bot-response-content');
                botResponseContent.innerHTML = result.content.replace(/\n/g, '<br>');
                const botReplyModal = new bootstrap.Modal(document.getElementById('botReplyModal'));
                botReplyModal.show();
            }
        } else {
            const botResponseContent = document.getElementById('bot-response-content');
            botResponseContent.innerHTML = `<i class="fas fa-exclamation-triangle me-2"></i>Error: ${result.error || 'Failed to send prompt'}`;
            const botReplyModal = new bootstrap.Modal(document.getElementById('botReplyModal'));
            botReplyModal.show();
        }
    } catch (error) {
        const botResponseContent = document.getElementById('bot-response-content');
        botResponseContent.innerHTML = `<i class="fas fa-exclamation-triangle me-2"></i>Error: ${error.message}`;
        const botReplyModal = new bootstrap.Modal(document.getElementById('botReplyModal'));
        botReplyModal.show();
    } finally {
        sendButton.disabled = false;
        sendButton.innerHTML = '<i class="fas fa-paper-plane me-1"></i>Send';
    }
}