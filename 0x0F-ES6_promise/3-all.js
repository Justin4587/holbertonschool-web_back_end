import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser]).then((txt) => {
    console.log(txt[0].body, createUser());
  }).catch(() => console.log('Signup system offline'));
}
