/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {

    const stack = []

    for(ast of asteroids){

        if(ast > 0){
            stack.push(ast)

        }else{
            if(!stack || stack[stack.length-1] < 0){
                stack.push(ast)

            } else {
                let used = false

                while(stack.length > 0 && stack[stack.length-1] > 0){
                    if(ast === stack[stack.length-1]*-1){
                        used = true
                        stack.pop()
                        break
                    } else if(stack[stack.length-1] > ast*-1){
                        used = true
                        break
                    } else {
                        stack.pop()
                    }
                }

                if(!used){
                    stack.push(ast)
                }
            }
        }
    }

    return stack

};