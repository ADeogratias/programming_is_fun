// Write a function to check if a string is a valid IP address
// Input: 12.32.11.33
// Output: true

/**
 * 1. Check falsy values
 * 2. Split string by .
 * 3.1. Check if its 4 array length\
 * 4. Go through the converted array
 * 4.1. Hard convert the current string to an integer
 * 4.1. Check if the converted number is invalid, less than 0 or greater than 255
 * 4.2. Store them in an array
 * 6. Check the new filtered array
 * 6.1. If its empty its a valid ip
 * 6.2. If not its not a valid ip
 */

/**
 *
 * @param {string} ipaddress
 */
function validateIpAddress(ipaddress) {
    if (!ipaddress) return false;

    const ipArray = ipaddress.split('.');
    if (!Array.isArray(ipArray) || ipArray.length !== 4) return false;

    const invalidIPArray = ipArray.filter((mask) => {
        const number = parseInt(mask);
        return isNaN(number) || number < 0 || number > 255;
    });
    if (invalidIPArray.length) return `Wrong octet: ${invalidIPArray}`;

    return true;
}

console.log(validateIpAddress('22.22.23.2'));
// 12.233.11.2
// asd.adsf.sadf
// asdfadsfadf
// 12232.11232.23.32231
// 0.0.0.0
// 255.255.255.255
// 88.990.001123
