$('.seleccionar').click(async (x) => {
    option = x.target.id
    console.log(JSON.stringify({id: option}))
    fetch('http://127.0.0.1:5000/selected', {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({id: option})
    })
})
