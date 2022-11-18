import { add } from '../src/index';
 
describe('testing index file', () => {
  test('empty string should result in zero', () => {
    expect(add('')).toBe(0);
  });
  test('1 plus two shoul result in 3', () => {
    expect(add('1,2')).toBe(3)
  })
  test('2 plus three shoul result in 5', () => {
    expect(add('2,3')).toBe(5)
  })

  test('negative number should result in error message', () => {
    expect(add('1,-1')).toThrow(new RangeError('Negatives are not allowed'))
  })
});