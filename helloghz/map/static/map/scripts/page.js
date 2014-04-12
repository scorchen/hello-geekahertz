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

}

$(document).ready(function () {
    initializeJQueryCode();
});