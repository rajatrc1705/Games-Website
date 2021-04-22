console.log('working');

var tableBody = document.getElementById('table-body');

const url = window.location.href
console.log(url)
var username = '';
$.ajax({
    type: 'GET',
    url: `${url}user/`,
    success: function(response){
        
        username = response.data;       
    },
    error: function(error){
        console.log(error)
    }
})
console.log(username)
$.ajax({
    type: 'GET',
    url: `${url}leaderdata`,
    success: function(response){
        var data = response.data;
        var rank = 1;
        for (var key in data){
            // var score = data[key];
            if (username == data[key][0]){
                var class_name = "bg bg-success"
            }
            else{
                var class_name = ""
            }
            tableBody.innerHTML += `
            <tr>
                <td class="${class_name}">${rank}</td>
                <td class="${class_name}">${data[key][0]}</td>
                <td class="${class_name}">${data[key][1]}</td>
            </tr>
            `
            rank = rank+1
        }
    },
    error: function(error){
        console.log(error);
    }
})