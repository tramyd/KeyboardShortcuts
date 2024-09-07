document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quizForm');
    const nextQuizButton = document.getElementById('nextQuiz');
    const resultMessage = document.getElementById('resultMessage');

    form.onsubmit = function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/quiz/3', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultMessage.textContent = data.message;
            Object.entries(data.correctAnswers).forEach(([question, isCorrect]) => {
                const correctInput = document.querySelector(`input[name="${question}"][value="${data[question]}"]`);
                const incorrectInputs = document.querySelectorAll(`input[name="${question}"]:not([value="${data[question]}"])`);

                // Style the selected answer
                if (correctInput) {
                    const label = correctInput.nextElementSibling;
                    label.style.color = isCorrect ? 'green' : 'red';
                }

                // Style other answers only if the selected was incorrect
                if (!isCorrect) {
                    incorrectInputs.forEach(input => {
                        const correctAnswer = document.querySelector(`input[name="${question}"][value="${data.answers[question]}"]`).nextElementSibling;
                        correctAnswer.style.color = 'green'; // Correct answer highlighted in green
                    });
                }
            });

            // Hide submit button and show next quiz link
            form.querySelector('button[type="submit"]').style.display = 'none';
            nextQuizButton.style.display = 'inline-block';
        })
        .catch(error => console.error('Error:', error));
    };
});
