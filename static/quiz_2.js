document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quizForm');
    const submitButton = document.querySelector('button[type="submit"]');
    const nextQuizButton = document.getElementById('nextQuiz');

    form.onsubmit = function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/quiz/2', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultMessage').textContent = data.message;
            // Highlight correct and incorrect answers
            Object.entries(data.correctAnswers).forEach(([key, value]) => {
                const questionDivs = document.querySelectorAll(`input[name=${key}]`);
                questionDivs.forEach((input) => {
                    const label = input.nextElementSibling;
                    if (input.value === data[key]) {
                        label.style.color = value ? "green" : "red";
                    }
                });
            });
            // Hide submit button and show next quiz link
            submitButton.style.display = 'none';
            nextQuizButton.style.display = 'inline-block';
        })
        .catch(error => console.error('Error:', error));
    };
});
