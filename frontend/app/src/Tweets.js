import React, {Component} from "react";
import io from "socket.io-client";

class Tweets extends Component {
    constructor(props) {
        super(props);
        this.socket = io('http://localhost:5000/tweet_streaming', {transports: ['websocket']})
        this.socket.on('tweet', tweet => this.setState(state => ({
            tweets: [...state.tweets, tweet]
        })));
    }

    componentDidMount() {
        this.socket.emit('subscribe', {track: ['python']});
    }

    componentWillUnmount() {
        this.socket.disconnect()
    }

    state = {
        tweets: []
    };

    render() {
        return (
            <div>
                <ul>
                    {this.state.tweets.map((tweet, index) => {
                        return <li key={index}>{tweet['author'] + ': ' + tweet['text']}</li>
                    })}
                </ul>
            </div>
        );
    }
}

export default Tweets;
