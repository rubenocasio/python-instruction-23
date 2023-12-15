// console.log("Yes, you made it to the script file.")

const jokesContainer = document.getElementById("jokes-container");
const jokeForm = document.getElementById('joke-form')
jokeForm.addEventListener('submit', handleSubmit)

function buildJokeCard(data){
    return `<div class="card shadow mb-3">
    <div class="card-body">${data.joke}</div>
    </div>`;
}

async function getDadJoke() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    const response = await fetch("https://icanhazdadjoke.com/", {
        headers: {
            Accept: 'application/json',
        },
    });
    // We then need to convert the data into JSON format.
    const data = await response.json();
    console.log(data)
    // return coderData;

    const jokeCard = buildJokeCard(data);
    jokesContainer.innerHTML += jokeCard
}


function handleSubmit(event){
    event.preventDefault()
    getDadJoke()
}

//Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.