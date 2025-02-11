$(document).ready(function(){
    $('.mainImg').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        fade: true,
        asNavFor: '.imgList',
        autoplay: true,
        autoplaySpeed: 2000,
        infinite: true,
    });
    $('.imgList').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.mainImg',
        centerMode: true,
        focusOnSelect: true,
        arrows: false,
        dots: false,
        infinite: true,
    });
});