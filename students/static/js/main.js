
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

function initDateFields() {

    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD',
        locale: 'uk'
    }).on('dp.hide', function (event){
        $(this).blur();
    });

}

function initDateFieldsExam() {
    $('input.datetimeinput').datetimepicker({
        'format': 'YYYY-MM-DD'
    }).on('dp.hide', function (event){
        $(this).blur();
    });
}

function initAddStudentForm(form, modal) {

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
        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
        'error': function(){
            alert('Помилка на серв.Спробуйте пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');

            modal.find('.modal-body').html(html.find('.alert'));

            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                initAddStudentForm(newform, modal);

            } else {
                setTimeout(function(){ location.reload(true);}, 500);
            }
            //$("#submit-id-add_button").prop("disabled", false);
            }
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

        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
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
            //$("#submit-id-add_button").prop("disabled", false);
    }
    });
}

function initEditGroupForm(form, modal) {
    initDateFields();

    form.find('input[name="cancel_button"]').click(function(event){

        modal.modal('hide');
        return false;
    });


    form.ajaxForm({
        'dataType': 'html',

        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
        'error': function(){
            alert('Помилка на серв.Спробуйте пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');
            modal.find('.modal-body').html(html.find('.alert'));
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                initEditGroupForm(newform, modal);
            } else {
                setTimeout(function(){ location.reload(true);}, 500);
            }
            $("#submit-id-add_button").prop("disabled", false);
    }
    });
}

function initAddGroupForm(form, modal) {
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
        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
        'error': function(){
            alert('Помилка на серв.Спробуйте пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');

            modal.find('.modal-body').html(html.find('.alert'));

            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                initAddGroupForm(newform, modal);

            } else {
                setTimeout(function(){ location.reload(true);}, 500);
            }
            $("#submit-id-add_button").prop("disabled", false);
            }
    });
}

function initEditExamForm(form, modal) {
    initDateFields();

    form.find('input[name="cancel_button"]').click(function(event){

        modal.modal('hide');
        return false;
    });

    form.ajaxForm({
        'dataType': 'html',

        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
        'error': function(){
            alert('Помилка на серв.Спробуйте пізніше.');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');
            modal.find('.modal-body').html(html.find('.alert'));
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                initEditExamForm(newform, modal);
            } else {
                setTimeout(function(){ location.reload(true);}, 500);
            }
            $("#submit-id-add_button").prop("disabled", false);
    }
    });
}

function initAddExamForm(form, modal) {
    initDateFields();

    form.find('input[name="cancel_button"]').click(function(event){

        modal.modal('hide');
        return false;
    });


    form.ajaxForm({
        'dataType': 'html',

        'beforeSend': function(xhr, settings){

            $("#submit-id-add_button").prop("disabled", true);
            $("#submit-id-cancel_button").prop("disabled", true);
            $('.form-horizontal').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
            },
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
            $("#submit-id-add_button").prop("disabled", false);
    }
    });
}

function initEditStudentPage() {

    var indicator_2 = $('#ajax-loader').html('<img id="loader-img"\\\n\
 src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $('a.student-edit-form-link').click(function(event) {
        var link = $(this);
        //$.blockUI();
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',

            'beforeSend': function(xhr, settings){
                indicator_2.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_2.hide();

            },
               // indicator.hide();
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_2.hide();
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
                indicator_2.hide();
                return false;
            }
        });
        return false;
    });
}

function initAddStudentPage() {
    var indicator_3 = $('#ajax-loader').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $("a#add_student").click(function(event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'beforeSend': function(xhr, settings){
                indicator_3.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_3.hide();

            },
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_3.hide();
                var modal = $('#myModal'),
                  html = $(data), form = html.find('#content-column form');
                  modal.find('.modal-title').html(html.find('#content-column h2').text());
                  modal.find('.modal-body').html(form);

                // init our edit form
             initAddStudentForm(form, modal);

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

function initEditGroupPage() {
    var indicator_4 = $('#ajax-loader').html('<img id="loader-img"\\\n\
 src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $('a.group-edit-form-link').click(function(event) {
        var link = $(this);
        //$.blockUI();
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',

            'beforeSend': function(xhr, settings){
                indicator_4.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_4.hide();

            },
               // indicator.hide();
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_4.hide();
                var modal = $('#myModal'),
                html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initEditGroupForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                 });
            },
            'error': function(){
                alert('Помилка на сервері.Спробуйте пізніше');
                indicator_4.hide();
                return false;
            }
        });
        return false;
    });
}

function initAddGroupPage() {
    var indicator_7 = $('#ajax-loader').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $("a#add_group").click(function(event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'beforeSend': function(xhr, settings){
                indicator_7.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_7.hide();

            },
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_7.hide();
                var modal = $('#myModal'),
                  html = $(data), form = html.find('#content-column form');
                  modal.find('.modal-title').html(html.find('#content-column h2').text());
                  modal.find('.modal-body').html(form);

                // init our edit form
             initAddGroupForm(form, modal);

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

function initEditExamPage() {
    var indicator_10 = $('#ajax-loader').html('<img id="loader-img"\\\n\
 src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $('a.exam-edit-form-link').click(function(event) {
        var link = $(this);
        //$.blockUI();
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',

            'beforeSend': function(xhr, settings){
                indicator_10.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_10.hide();

            },
               // indicator.hide();
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_10.hide();
                var modal = $('#myModal'),
                html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initEditExamForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                 });
            },
            'error': function(){
                alert('Помилка на сервері.Спробуйте пізніше');
                indicator_10.hide();
                return false;
            }
        });
        return false;
    });
}

function initAddExamPage() {
    var indicator_3 = $('#ajax-loader').html('<img id="loader-img" \\\n\
src="/static/img/ajax-loader.gif"  width="100" height="20" /> Now loding... ');
    $("a#add_exam").click(function(event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'beforeSend': function(xhr, settings){
                indicator_3.show();
            },
            'error': function(xhr, status, error){
                alert(error);
                indicator_3.hide();

            },
            'success': function(data, status, xhr){
                if (status != 'success') {
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }
                indicator_3.hide();
                var modal = $('#myModal'),
                  html = $(data), form = html.find('#content-column form');
                  modal.find('.modal-title').html(html.find('#content-column h2').text());
                  modal.find('.modal-body').html(form);

                // init our edit form
             initAddExamForm(form, modal);

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

//function refreshpage() {
//    $('#refresh').click(function(event){
//        var link = $(this);
//        $.ajax({
//            'url': link.attr('href'),
//            'type': 'get',
//            'dataType': 'html',
//
//            'beforeSend': function(xhr, settings){
//
//            },
//            'error': function(xhr, status, error){
//                alert(error);
//
//            },
//            'success': function(data, status, xhr){
//
//            }
//        });
//    });
//}



$(document).ready(function(){
    initJournal();
    initGroupSelector();
    initDateFields();
    initDateFieldsExam();
    initEditStudentPage();
    initAddStudentPage();
    initEditGroupPage();
    initAddGroupPage();
    initEditExamPage();
    initAddExamPage();
    //refreshpage();
});