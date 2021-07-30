import PropTypes from 'prop-types'
// rafce
const Button = ({ color, text, onClick }) => {
    
    return (
        <button 
            onClick={onClick} 
            style={{ backgroundColor: color }} 
            className='btn'
        >
            {text}
        </button>
    ) 
}

Button.defaulfProps = {
    color: 'steelblue',
}

Button.protoTypes = {
    text: PropTypes.string,
    color: PropTypes.string,
}

export default Button
