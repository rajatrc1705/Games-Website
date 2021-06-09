const url = window.location.href
console.log(url);
const resultBox = document.getElementById('result-box')
const bodyTable = document.getElementById('body-table')

// this displays the result after the user submits the quiz, the data is retrieved through a GET request
// show_quiz_result function in views.py
$.ajax({
    type: 'GET',
    url: `${url}result/`,
    success: function(response){
        var data = response.data
        
        for (var key in data){
            console.log(data[key])

            // highlighting the score of the user in the Scorecard
            if (key == 'Score'){
                class_name="table-success"
            }
            else{
                class_name="table-dark"
            }
            bodyTable.innerHTML += `
                    <tr>
                    <td class="${class_name}">${key}</td>
                    <td class="${class_name}">${data[key]}</td>
                    </tr>
                `
        }
        
        if (data['Score'] == data['Maximum Marks']){
            resultBox.innerHTML += `
            <br><br>
            <div class="alert alert-success" role="alert">
                <h4 class="alert-heading">Well done!</h4>
                <p>You Have Scored A Perfect Score.</p><hr>
                <p class="mb-0">Well Done, Keep It Going!</p>
            </div>
            `
        }
    },
    error: function(error){
        console.log(error)
    }
})
