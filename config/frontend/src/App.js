import React from 'react';
import { BrowserRouter as Router , Route, Switch} from 'react-router-dom';
import { Header } from './Header';
import { Top } from './Top';
import { DailyTop } from './daily/pages/DailyTop';
import { CategoryView } from './daily/pages/CategoryView';
import {DailyDetail} from './daily/pages/DailyDetail';
import { Profile} from './profile/Profile';

export const App = () => {
    return(
        <div>
            <Router>
                <Header></Header>
                <div>
                    <Switch>
                        
                    </Switch>
                </div>
            </Router>
        </div>
    )
}