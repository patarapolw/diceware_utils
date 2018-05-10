$(document).ready(function() {
    $("#do_generate_password").click(function(event) {
        event.preventDefault();
        $.post('/generate_password', $("#generate_password_form").serialize(), function(data, textStatus, xhr) {
            $("#generated_password").html(data);
            $("#visible_keywords").val($("#keywords").val());
        });
    });

    $("#do_randomize_words").click(function(event) {
        $.post('/randomize_words', function(data, textStatus, xhr) {
            $("#keywords").val(data);
            $("#do_generate_password").click();
        });
    });

    $("#do_generate_sentence").click(function(event) {
        event.preventDefault();
        $.post('/generate_sentence', $('#generate_sentence_form').serialize(), function(data, textStatus, xhr) {
            $("#generated_sentence").html(data);
        });
    });

    $("#do_randomize_words").click();
});
