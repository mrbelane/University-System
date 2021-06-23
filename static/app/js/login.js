// Click on Labels
$(".form__label").click(function() {
  if ($(this).hasClass('is-closed')) {
    $("input[id='" + $(this).attr('for') + "']").removeClass("is-closed");
    $(this).removeClass('is-closed');
  }
});

// // Focus on Inputs
// $(".form__input").focus(function() {
//   if ($(this).hasClass('is-closed')) {
//     $("label[for='" + $(this).attr('id') + "']").removeClass("is-closed");
//     $(this).removeClass('is-closed');
//   }
// });
//
// // Click on Submit
// $(".form__submit").click(function(e) {
//   e.preventDefault();
//   $(this).addClass('form__submit--animated');
//   $('.reset').removeClass('reset--hide');
// });
//
// // Click on reset
// $(".reset").click(function() {
//   $('.form__label').addClass('is-closed');
//   $('.form__input').addClass('is-closed').val('');
//   $('.form__submit').removeClass('form__submit--animated');
//   $('.reset').addClass('reset--hide');
// });