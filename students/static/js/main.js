function initJournal() {
    var indicator = $('#ajax-progress-indicator');
    var error_ajax = $('#error-ajax');
    $('.day-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1': '',
                'csrfmiddlewaretoken':
                    $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function(xhr, settings){
                indicator.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator.hide();
                error_ajax.show();
            },
            'success': function(data, status, xhr){
                indicator.hide();
                error_ajax.hide();
            }
        });
    });
}

function initGroupSelector() {
    $('#group-selector select').change(function (event){
        var group = $(this).val();
        if (group) {
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
        }  else {
            $.removeCookie('current_group', {'path': '/'});
        }
        location.reload(true);
        return true;
        });
}

function initEditStudentForm(form, modal) {
    initDateFields();
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });

    form.ajaxForm({
        'dataType': 'html',
        'error': function(){
            alert('Помилка на серв.Спробуйте пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');
            modal.find('.modal-body').html(html.find('.alert'));
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                initEditStudentForm(newform, modal);
            } else {
                setTimeout(function(){ location.reload(true);}, 500);
            }

    }
    });
}



function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'
    }).on('dp.hide', function (event){
        $(this).blur();
    });
}
function initDateFieldsExam() {
    $('input.datetimeinput').datetimepicker({
        'format': 'YYYY-MM-DD h:mm:ss'
    }).on('dp.hide', function (event){
        $(this).blur();
    });
}
function initEditStudentPage() {
    $('a.student-edit-form-link').click(function(event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                var modal = $('#myModal'),
                html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initEditStudentForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                });
            },
            'error': function(){
                alert('Помилка на сервері.Спробуйте пізніше');
                return false;
            }
        });
        return false;
    });
}

$(document).ready(function(){
    initJournal();
    initGroupSelector();
    initDateFields();
    initDateFieldsExam();
    initEditStudentPage();
});