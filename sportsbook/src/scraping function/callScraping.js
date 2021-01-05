function callPython() { 
    var spawn = require("child_process").spawn; 
     
    var process = spawn('python', ["c:/Users/aaron/Git/sports-web-scraping/sportsbook/src/scraping function/scraping.py"]); 
  
    process.stdout.on('close', function() { 
        console.log('Scraping complete'); 
    }) 

    process.stderr.on('data', function() { 
        console.log('Scraping error'); 
    }) 
} 

callPython()