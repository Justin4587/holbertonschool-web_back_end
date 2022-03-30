export default function uploadPhoto(filename) {
  const bs = ' cannot be processed';
  return Promise.reject(new Error(filename + bs));
}
