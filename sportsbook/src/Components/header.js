import React from 'react';

const Header = () => {    
    const today = new Date();
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1)
    const todayString = today.toLocaleString('default', { month: 'long', day: '2-digit'});
    const tomorrowString = tomorrow.toLocaleString('default', { month: 'long', day: '2-digit'});
    
    return (
        <div>
            <form className='form'>
                <label className='label'>Select sport and date:</label>
                <select name='sport' className='select'>
                    <option value='/betting-odds/nfl-football'>
                        NFL
                    </option>
                    <option value='/betting-odds/college-football'>
                        NCAA FB
                    </option>
                </select>
                <select date='date' className='select'>
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