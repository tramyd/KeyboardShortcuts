document.addEventListener('DOMContentLoaded', function() {
    const correctSequence = ['Ctrl', 'D'];  // Correct keys for bookmarking a page in many browsers
    let userInput = [];

    document.querySelectorAll('.key').forEach(key => {
        key.addEventListener('click', function() {
            userInput.push(this.getAttribute('data-key'));
            document.getElementById('status').textContent = '';  // Clear status message on new input
            checkSequence();
        });
    });

    function checkSequence() {
        if (userInput.length === correctSequence.length) {
            if (JSON.stringify(userInput) === JSON.stringify(correctSequence)) {
                updateStatus("Correct sequence!");
                incrementCorrectCount();  // Call to increment the count on the server
            } else {
                updateStatus("Incorrect sequence. Proceeding to the next question.");
            }
            userInput = [];  // Reset input after checking
            document.getElementById('finishQuiz').style.display = 'block';  // Show the "Next" button
        }
    }

    function updateStatus(message) {
        document.getElementById('status').textContent = message;
    }

    function incrementCorrectCount() {
        fetch('/increment_correct_count', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log(`Correct count: ${data.correctCount}`);
        })
        .catch(error => console.error('Error incrementing count:', error));
    }
});