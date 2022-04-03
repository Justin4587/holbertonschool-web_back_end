import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser()]).then((txt) => {
    const txt0 = txt[0].body;
    const txt1 = txt[1].firstName;
    const txt2 = txt[1].lastName;
    const message = txt0 + ' ' + txt1 + ' ' + txt2;
    console.log(message);
  }).catch(() => console.log('Signup system offline'));
}
