$(document).ready(function () {
    let timeout = null;

    $('#text-input').on('input', function () {
        clearTimeout(timeout);
        const text = $(this).val();

        timeout = setTimeout(function () {
            $.ajax({
                url: '/api/translate/',
                type: 'POST',
                data: {
                    text: text,
                },
                success: function (response) {
                    $('#translation').text(response.translation);
                },
                error: function (error) {
                    console.error('Translation request failed', error);
                }
            });
        }, 5000);
    });
});