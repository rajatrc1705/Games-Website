console.log('You are in quiz')
const url = window.location.href
const quizBox = document.getElementById('quiz-box');

$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function(response){
        
        /* response will contain the JsonResponse which contains the data about the questions and their possible answers*/
        const data = response.data
        const image = response.image
        var count = 0;
        data.forEach(element=>{
            for (const [question, answers] of Object.entries(element)){
                quizBox.innerHTML += `
                    <figure class="figure">
                        <img src="${image[count]}" class="figure-img img-fluid rounded" width="350" height="270" alt="Harry Potter">
                    </figure>
                    <div class="card" >
                    <div class="card-header">
                        ${question}<br>
                    </div>
                    
                    <ul class="list-group list-group-flush">
                        
                `   
                count = count + 1;

                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <li class="list-group-item">
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                        </li>
                        
                    `
                })
                quizBox.innerHTML += `
                    </ul>
                    </div>
                    <br><hr>
                `
            }
        })
    },
    error: function(error){
        console.log(error)
    }
})


const quizForm = document.getElementById('quiz-form');
const csrf_token = document.getElementsByName('csrfmiddlewaretoken')

const sendData = ()=>{
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf_token[0].value
    console.log(elements)
    elements.forEach(el=>{
    
        if (el.checked){
            data[el.name] = el.value
        }
        else{
            if (!data[el.name]){            
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            /* This text works */
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
    window.location.href = url + 'res'
})