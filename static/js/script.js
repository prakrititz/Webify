$(function() {
    var swiper = new Swiper('.carousel-gallery .swiper-container', {
        effect: 'slide',
        speed: 900,
        slidesPerView: 5,
        spaceBetween: 20,
        simulateTouch: true,
        autoplay: {
            delay: 5000,
            stopOnLastSlide: false,
            disableOnInteraction: false
        },
        pagination: {
            el: '.carousel-gallery .swiper-pagination',
            clickable: true
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 5
            },
            425: {
                slidesPerView: 2,
                spaceBetween: 10
            },
            768: {
                slidesPerView: 3,
                spaceBetween: 20
            }
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // function selectTemplate(template) {
    //     document.getElementById('selected_template').value = template;
    //     document.querySelectorAll('.template-option').forEach(option => {
    //         option.classList.remove('selected');
    //     });
    //     event.currentTarget.classList.add('selected');
    // }
    // window.selectTemplate = selectTemplate;

    // function selectPalette(palette) {
    //     document.getElementById('selected_palette').value = palette;
    //     document.querySelectorAll('.palette-option').forEach(option => {
    //         option.classList.remove('selected');
    //     });
    //     event.currentTarget.classList.add('selected');
    // }
    // window.selectPalette = selectPalette;
});

function selectTemplate(template, element) {
    document.getElementById('selected_template').value = template;
    document.getElementById('selected-template-text').textContent = 'Selected template: ' + template;
    document.querySelectorAll('.template-option').forEach(option => {
        option.classList.remove('selected');
    });
    element.classList.add('selected');
}

function selectPalette(palette, element) {
    document.getElementById('selected_palette').value = palette;
    document.getElementById('selected-palette-text').textContent = 'Selected palette: ' + palette;
    document.querySelectorAll('.palette-option').forEach(option => {
        option.classList.remove('selected');
    });
    element.classList.add('selected');
}

$('.txt').html(function(i, html) {
    var chars = $.trim(html).split("");
    return '<span>' + chars.join('</span><span>') + '</span>';
});
