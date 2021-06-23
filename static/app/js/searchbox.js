var seaechbox=$('.txtsearchbox');

seaechbox.click(function () {
    $(this).animate({'width':'270'},800);
});

seaechbox.mouseleave(function () {
    $(this).animate({'width':'100'},800);
});

$('.h').hover(function () {
    $(this).animate({'height':'160'},400);
}, function () {

    $(this).animate({'height':'40'},400);
});