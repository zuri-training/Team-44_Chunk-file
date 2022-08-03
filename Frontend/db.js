import mongoose from 'mongoose';

// Schema Template is subjected to change depending on progress

const postSchema = mongoose.Schema({
  id: number,
  username: String,
  email: String,
  password: String,
  tags: [String],
  selectedFile: String,
  createdAt: {
    type: Date,
    default: new Date(),
  },
});

var PostData = mongoose.model('PostData', postSchema);

export default PostData;
