function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var initHomePage = function(){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/files/',
        contentType: 'application/json',
        type: 'GET',
        success: function(response){
            
            var tbody = $('#tbody');
            for(var i = 0; i < response.length; i++)
            {                
                tbody.append('<tr><td>'+response[i].filename+'</td><td>'+response[i].file_size+' Bytes</td><td>'+response[i].upload_date+'</td><td><form id="'+response[i].id+'" class="delete-form" method="DELETE"><input type="submit" class="btn btn-danger" value="Delete"></td></tr></form>');
            }
        }
    });
    
}

$(document).ready(function(){
    initHomePage();
    
    //upload file via REST API
    $('form').submit(function(e){
        e.preventDefault();

        var formData = new FormData(this);
        formData.append('file', $('#file-upload-field').val());
        
        $.ajax({
            url: 'http://127.0.0.1:8000/api/upload/',
            data: formData,
            method: 'POST',
            contentType: false,
            processData: false,
            success: function(){
                location.reload();
            }
        })
    });

    //delete a file via REST API
    $('#tbody').on('submit', '.delete-form', function(e){
        e.preventDefault();
        var _url = 'http://127.0.0.1:8000/api/files/' + $(this).attr('id') + '/';
        fetch(_url,{
            method: 'DELETE',
            headers:{
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        }).then((response) => {
            location.reload();
        })
    });

    //search
    $('#search-button').click(function(e){
        e.preventDefault();
        //bar chart variables
        var labels = []
        var frequency = []
        var searchWord = $('#search-field').val();
        $('#word').html(searchWord);
        $('#search-field').val('') //clear the search field
        $.ajax({
            url: 'http://127.0.0.1:8000/api/search/',
            data: {'search_word': searchWord},
            method:'GET',

            success: function(response){
                $('#search-results').html('');
                for(var i = 0; i < response['data'].length; i++)
                    if(response['data'][i][1] != 0)
                    {
                        $('#search-results').append('<li>'+response['data'][i][0]+' - Frequency: '+response['data'][i][1]+'</li>');
                        labels.push(response['data'][i][0]);
                        frequency.push(response['data'][i][1]);
                    }
                        
                
            },
            error: function(e){
                alert('Error');
            }
        });

        frequency.push(0);
        var ctx = document.getElementById('frequency-dist');
        var barChart = new Chart(ctx,{
            type: 'bar',
            data: {
                labels: labels,
                datasets:[{
                    label: 'Frequency Distribution',
                    data: frequency,
                    backgroundColor: [
                        'rgba(0, 255, 0, 0.2)',
                        'rgba(255, 0, 0, 0.2)'
                    ]
                }]
            },
            options: {
                maintainAspectRation: false,            
            }
        });
    });

    //logout user via REST API
    $('#logout').click(function(e){
        e.preventDefault();
        $.ajax({
            url: 'http://127.0.0.1:8000/api/dj-rest-auth/logout/',
            dataType: 'application/json',
            contentType: 'application/json',
            method: 'POST',
            beforeSend: function(request){
                try{
                    request.setRequestHeader('Authorization', 'Token' + localStorage.getItem('auth').key);
                }catch(error){
                    request.setRequestHeader('Authorization', 'Token' + sessionStorage.getItem('auth').key);
                }
                
            },
            success: function(){
                
            }            
        })
    });

    $('#login').click(function(e){
        
    });
})