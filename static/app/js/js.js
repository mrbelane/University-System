$('.input').each(function () {
    var input = $(this);
    var div_mt = $('<div />').addClass('material-input');
    input.replaceWith(div_mt);
    div_mt.append(input);
    var placeHolder = input.attr('placeholder');
// alert(placeHolder)
    div_mt.prepend($('<label />').addClass('material-label').text(placeHolder));
    input.attr('placeholder', '')

})

$('.input').focus(function () {
    // var _this = $(this);
    // var div_mt = _this.parent();
    // console.log(div_mt);
    // div_mt.addClass('is-active is-up');
    $(this).parent().addClass('is-active is-up');
})

$('.input').focusout(function () {

    if (!$(this).val().toString().length) {
        $(this).parent().removeClass('is-up');
    }
    $(this).parent().removeClass('is-active');
})