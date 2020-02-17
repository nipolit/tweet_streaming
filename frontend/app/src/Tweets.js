import React, {Component} from "react";
import PropTypes from 'prop-types';
import io from "socket.io-client";
import Toast from "react-bootstrap/Toast";

class Tweets extends Component {
    static propTypes = {
        track: PropTypes.string.isRequired
    };

    constructor(props) {
        super(props);
        this.socket = io('http://localhost:5000/tweet_streaming')
        this.socket.on('tweet', tweet => this.setState(state => ({
            tweets: [tweet, ...state.tweets]
        })));
    }

    componentDidMount() {
        this.socket.emit('subscribe', {track: [this.props.track]});
    }

    componentWillUnmount() {
        this.socket.disconnect()
    }

    state = {
        tweets: []
    };

    render() {
        return (
            this.state.tweets.map((tweet, index) => {
                return (
                    <Toast>
                        <Toast.Header closeButton={false}>
                            <strong className="mr-auto">{tweet['author']}</strong>
                        </Toast.Header>
                        <Toast.Body>{tweet['text']}</Toast.Body>
                    </Toast>
                );
            })
        );
    }
}

export default Tweets;
