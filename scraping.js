const axios = require('axios')


function fetchNCAAFBteams() {
    axios
        .get('https:/u002F/u002Foddscdn.sportsbookreview.com/u002F')
        .then(res => {
            let data = res.data;
            console.log(data)
            return data
        })
}

fetchNCAAFBteams()