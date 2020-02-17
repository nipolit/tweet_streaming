import React, {Component} from "react";
import InputGroup from "react-bootstrap/InputGroup";
import FormControl from "react-bootstrap/FormControl";
import Button from "react-bootstrap/Button";
import Tweets from "./Tweets";

class TrackTopic extends Component {

    constructor(props) {
        super(props);
        this.inputRef = React.createRef();
    }

    state = {
        topic: ''
    };

    handleClick() {
        this.setState(state => ({
            topic: this.inputRef.current.value
        }));

    }

    render() {
        console.log(this.state.topic)
        return (
            <div align="center">
                <InputGroup>
                    <FormControl
                        placeholder="Twitter topic"
                        ref={this.inputRef}
                    />
                    <InputGroup.Append>
                        <Button variant="outline-secondary"
                                onClick={() => this.handleClick()}>Start tracking</Button>
                    </InputGroup.Append>
                </InputGroup>
                {!!this.state.topic.trim() &&
                <Tweets key={`tweets-${this.state.topic}`} track={this.state.topic}/>
                }
            </div>
        );
    }
}

export default TrackTopic
