function getFinalOpenedDoors(numDoors) {
  const l = numDoors + 1;
  let doors = Array.from({ length: l }, () => false);

  for (let door = 1; door < l; door++) {
    for (let step = door; step < l; step += door) {
      doors[step] = !doors[step];
    }
  }

  return doors
    .map((v, i) => {
      if (v) return i;
    })
    .filter((v) => v !== undefined);
}

console.log(getFinalOpenedDoors(100));
