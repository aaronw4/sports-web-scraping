import React, { useState } from 'react';

const Header = () => {    
    const today = new Date();
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1)
    const todayString = today.toLocaleString('default', { month: 'long', day: '2-digit'});
    const tomorrowString = tomorrow.toLocaleString('default', { month: 'long', day: '2-digit'});
    
    const [sport, setSport] = useState('/betting-odds/nfl-football');
    const [date, setDate] = useState(todayString);

    function handleSport(e) {
        setSport(e.target.value)
    }

    function handleDate(e) {
        setDate(e.target.value)
    }

    function postData(input) {
        // $.ajax({
        //     type: "POST",
        //     url: "/reverse_pca.py",
        //     data: { param: input },
        //     success: postComplete
        // });
    }
    
    function postComplete(e) {
       e.preventDefault();
    }

    function handleSubmit(e) {
        e.preventDefault();
        console.log(sport, date)
    }

    return (
        <div>
            <form onSubmit={handleSubmit} className='form'>
                <label className='label'>Select sport and date:</label>
                <select name='sport' onChange={handleSport} className='select'>
                    <option value='/betting-odds/nfl-football'>
                        NFL
                    </option>
                    <option value='/betting-odds/college-football'>
                        NCAA FB
                    </option>
                </select>
                <select date='date' onChange={handleDate} className='select'>
                    <option value={todayString}>
                        {todayString}
                    </option>
                    <option value={tomorrowString}>
                        {tomorrowString}
                    </option>
                </select>
                <button className='submit'>Submit</button>
            </form>
        </div>
    )
}

export default Header