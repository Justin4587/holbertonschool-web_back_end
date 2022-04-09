process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const strin = process.stdin.read();
  if (strin) {
    const your = 'Your name is: ';
    process.stdout.write(your + strin);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
