# Fashion Assistant for Visually Impaired

An intelligent fashion recommendation system that combines voice interaction and web scraping to help visually impaired individuals explore and choose clothing.

## 🎯 Project Overview

This project aims to create an accessible fashion assistant that transforms visual fashion information into voice-based interactions, making online fashion shopping more inclusive for visually impaired users.

## ✨ Key Features

### 1. Web Scraping Fashion Data
- Scrapes clothing information from major fashion retailers (e.g., H&M, Prada)
- Collects detailed product information including:
  - Product names
  - Colors
  - Materials
  - Descriptions
  - Patterns
  - Images

### 2. Image Processing
- Utilizes CLIP (Contrastive Language-Image Pre-Training) model
- Converts fashion images into vector embeddings for efficient similarity search
- Enables content-based image retrieval and matching

### 3. Natural Language Generation
- Transforms technical product descriptions into natural, conversational recommendations
- Uses ChatGPT to generate human-like fashion advice
- Creates contextual and personalized clothing suggestions

### 4. Voice Interface
- **Input**: Google Speech Recognition for converting user voice commands to text
- **Output**: OpenAI Text-to-Speech for delivering fashion recommendations in natural voice

## 🔧 Technical Stack

- **Web Scraping**: Python web scraping tools
- **Image Processing**: CLIP (OpenAI)
- **Language Model**: ChatGPT API
- **Speech Processing**:
  - Google Speech Recognition (STT)
  - OpenAI Text-to-Speech (TTS)

## 🎯 Goal

The primary goal is to bridge the gap in online fashion shopping for visually impaired individuals by providing an intuitive, voice-based interface for exploring and receiving personalized fashion recommendations.

## 💡 Use Case

1. User provides voice input about their fashion preferences
2. System processes the voice command into text
3. Matches user preferences with the fashion database
4. Generates personalized recommendations using natural language
5. Delivers recommendations through voice output

## 🚀 Future Enhancements

- Expand retailer database
- Implement personalized style learning
- Add multi-language support
- Integrate with e-commerce platforms
- Enhance recommendation algorithms
