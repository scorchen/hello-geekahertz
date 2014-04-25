/**
 * Created by scorchen on 4/9/14.
 */
function initializeJQueryCode(rootselector) {
    if (rootselector == null) rootselector = document;

    $('.focus-control', rootselector).focus();
    $('.field-validation-error', rootselector).click(function () { $(this).hide(); });
    $('input[data-val-required]', rootselector).addClass('required-field').each(function () { $("label[for='" + $(this).attr('id') + "']").addClass('required-field'); });
    $('select[data-val-required]', rootselector).addClass('required-field').each(function () { $("label[for='" + $(this).attr('id') + "']").addClass('required-field'); });
    $('textarea[data-val-required]', rootselector).addClass('required-field').each(function () { $("label[for='" + $(this).attr('id') + "']").addClass('required-field'); });
    $('.image-link').magnificPopup({ type: 'image' });
  
    $('.video-popup').magnificPopup({
        type: 'iframe',
        closeOnContentClick: true,
        gallery: {
            enabled: true
        }
    });
   
    $('.video').magnificPopup({
        type: 'iframe',
        iframe: {
          
            patterns: {
                youtube: {
                    index: 'youtube.com/', // String that detects type of video (in this case YouTube). Simply via url.indexOf(index).

                    id: 'v=', // String that splits URL in a two parts, second part should be %id%
                    // Or null - full URL will be returned
                    // Or a function that should return %id%, for example:
                    // id: function(url) { return 'parsed id'; } 

                    src: '//www.youtube.com/embed/%id%?autoplay=1' // URL that will be set as a source for iframe. 
                }

                // you may add here more sources

            },

            srcAction: 'iframe_src', // Templating object key. First part defines CSS selector, second attribute. "iframe_src" means: find "iframe" and set attribute "src".
        }


    });
}

$(document).ready(function () {
    initializeJQueryCode();
});