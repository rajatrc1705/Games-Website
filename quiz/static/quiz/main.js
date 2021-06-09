
const modalButtons = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body');
const startButton = document.getElementById('start-button');
const userId = document.getElementById('user-id');

var url = window.location.href;
console.log(url)
$.ajax({
    type: 'GET',
    url: `${url}user/`,
    success: function(response){

        const data = response.data;
        console.log(data)        
        userId.innerHTML += `
            <p>Username : ${data}</p>
        `
    },
    error: function(error){
        console.log(error)
    }
})

// displays the information for the particular quiz
modalButtons.forEach(button=> button.addEventListener('click', ()=>{
    const pk = button.getAttribute('data-pk')
    const name = button.getAttribute('data-quiz')
    const num_questions = button.getAttribute('data-questions')
    const time = button.getAttribute('data-time')
    const max_marks = button.getAttribute('data-maxmarks')

    modalBody.innerHTML = `
        <div class="mb-3">Are you ready to begin the quiz?
        <ul>
            <li>Name: <strong>${name}</strong></li>
            <li>Questions: <strong>${num_questions}</strong></li>
            <li>Time: <strong>${time}</strong></li>
            <li>Max Marks: <strong>${max_marks}</strong></li>
        </ul>
        </div>
    `

    startButton.addEventListener('click', ()=>{
        window.location.href = url + pk        
    })
}));