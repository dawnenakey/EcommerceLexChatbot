import { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import { Auth, API } from 'aws-amplify';

export default function App() {
  const [lesson, setLesson] = useState('');

  useEffect(() => {
    fetchLesson();
  }, []);

  const fetchLesson = async () => {
    const user = await Auth.currentAuthenticatedUser();
    const response = await API.get('api', '/lesson', {
      headers: { Authorization: user.signInUserSession.idToken.jwtToken }
    });
    setLesson(response.url);
  };

  return (
    <View>
      <Text>Lesson: {lesson || 'Loading...'}</Text>
      <Button title="Refresh" onPress={fetchLesson} />
    </View>
  );
}
