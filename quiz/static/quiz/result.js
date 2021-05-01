

const url = window.location.href
console.log(url);
const resultBox = document.getElementById('result-box')
const bodyTable = document.getElementById('body-table')
$.ajax({
    type: 'GET',
    url: `${url}result/`,
    success: function(response){
        var data = response.data
        console.log(url)
        console.log(data)
        // data = JSON.parse(data)
        // data = JSON.parse(JSON.stringify(data))
        
        for (var key in data){
            console.log(data[key])
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
        // data.forEach(element=>{
        //     for (const [key, value] in Object.entries(element)){
        //         resultBox.innerHTML += `
        //             <div class="p-2"> 
        //                 ${key}: ${value}
        //             </div>
        //             <br>
        //         `
        //     }
        // })
    },
    error: function(error){
        console.log(error)
    }
})

// const button = document.getElementById('return-main');
// button.addEventListener('submit', e=>{
//     window.location.href = url
// })