
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

modalButtons.forEach(button=> button.addEventListener('click', ()=>{
    const name = button.getAttribute('data-game')
    const url_game = button.getAttribute('data-url')
    console.log("AYA")
    modalBody.innerHTML = `
        <div class="mb-3">Are you ready to begin the quiz?
        <ul>
            <li>Name: <strong>${name}</strong></li>
            <li><a href="${url_game}"></a></li>
        </ul>
        </div>
    `

    startButton.addEventListener('click', ()=>{
        console.log(url_game)
        // if (name == 'Frage'){
        //     window.location.href = 'http://127.0.0.1:8000/'
        // }
        // else{
        //     window.location.href = url_game
        // }      
        window.location.href = url_game
    })
}));