#define PROCESSING_TEXTURE_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
	vertColor = color;
	vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);

	vec4 p = texture2D(texture, vec2(vertTexCoord.x, vertTexCoord.y));
	float gray = 200 * (p.r * 0.3 + p.g * 0.6 + p.b * 0.1);

	vec4 pos = position + vec4(gray * normal.x, gray * normal.y, gray * normal.z, 0.0);
	gl_Position = transform * pos;
}
