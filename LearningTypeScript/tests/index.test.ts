import { add } from '../src/index';
 
describe('testing index file', () => {
  test('empty string should result in zero', () => {
    expect(add('')).toBe(0);
  });
  test('1 plus two shoul result in 3', () => {
    expect(add('1,2')).toBe(3)
  })
});