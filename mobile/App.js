import Amplify, { Interactions } from 'aws-amplify';
import awsconfig from './aws-exports';
import { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';

Amplify.configure(awsconfig);

export default function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async () => {
    const lexResponse = await Interactions.send('ECommerceBot', message);
    setResponse(lexResponse.message);
  };

  return (
    <View>
      <TextInput
        value={message}
        onChangeText={setMessage}
        placeholder="Type your message"
      />
      <Button title="Send" onPress={sendMessage} />
      <Text>{response}</Text>
    </View>
  );
}
