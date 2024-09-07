let firstSelection = null;
let pairsFound = 0;
const totalPairs = 3;  // Total number of pairs to match

document.addEventListener('DOMContentLoaded', () => {
    const actionButtons = document.querySelectorAll('.action-button');
    const shortcutButtons = document.querySelectorAll('.shortcut-button');
    const resultMessage = document.getElementById('resultMessage');
    const nextQuizButton = document.getElementById('nextQuiz');
    const skipQuizButton = document.getElementById('skipQuiz');  // Reference to the skip button

    [...actionButtons, ...shortcutButtons].forEach(button => {
        button.addEventListener('click', (event) => {
            handleButtonClick(event.target);
        });
    });

    function handleButtonClick(button) {
        if (!firstSelection) {
            firstSelection = button;
            button.classList.add('selected');
        } else {
            if (firstSelection.dataset.match === button.dataset.match && firstSelection !== button) {
                incrementCorrectCount();
                pairsFound++;
                firstSelection.remove();
                button.remove();
                if (pairsFound === totalPairs) {
                    // When all pairs are matched, show the correct count and next button
                    fetchCorrectCount().then(() => {
                        nextQuizButton.style.display = 'block';  // Show the next button
                        skipQuizButton.style.display = 'none';  // Hide the skip button
                        resultMessage.textContent = `All pairs matched! Total correct answers: ${pairsFound}`;
                    });
                }
                firstSelection = null;
            } else {
                if (pairsFound !== totalPairs) {  // Only show the message if not all pairs are matched
                    resultMessage.textContent = 'Incorrect pair. Try again!';
                }
                firstSelection.classList.remove('selected');
                firstSelection = null;
            }
        }
    }

    function incrementCorrectCount() {
        fetch('/increment_correct_count', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log('Correct count incremented:', data.correctCount);
        })
        .catch(error => console.error('Error incrementing count:', error));
    }

    function fetchCorrectCount() {
        return fetch('/get_correct_count', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            pairsFound = data.correctCount;  // Update local correct count
        })
        .catch(error => console.error('Error fetching count:', error));
    }
});
