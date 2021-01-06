var express = require('express');
var server = express();
var data = require('../odds.json')

server.listen(5000, () => {
    console.log('Server running on port 5000')
});

server.get('/scraping', callPython);

function callPython(req, res) { 
    var spawn = require("child_process").spawn; 
     
    var process = spawn('python', [
        "c:/Users/aaron/Git/sports-web-scraping/sportsbook/src/scrapingFunction/scraping.py",
        req.query.sport,
        req.query.date
    ]); 
  
    process.stdout.on('close', function() { 
        res.send(data) 
    }) 

    process.stderr.on('data', function() { 
        console.log('Scraping error'); 
    }) 
} 

// callPython('/betting-odds/nba-basketball', 'January 05')