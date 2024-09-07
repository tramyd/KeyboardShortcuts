document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const userInput = document.getElementById('user_input').innerHTML.trim();
        const hiddenInput = document.getElementById('hidden_input');
        hiddenInput.value = userInput; // Set the hidden input value to the HTML content

        const correctFormat = '<u>User</u> <strong>Interface</strong> <em>Design</em>';
        if (userInput !== correctFormat) {
            alert('Please format the text exactly as specified: Underlined "User", Bold "Interface", Italic "Design".');
            event.preventDefault();  // Stop the form from submitting
        }
    });
});
